param(
    [ValidateRange(1, 24)]
    [int]$Hours = 8
)

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "Configurando acceso temporal a MongoDB Atlas..."

# ------------------------------------------------------------
# 1. Comprobar Atlas CLI
# ------------------------------------------------------------

$atlasCommand = Get-Command atlas -ErrorAction SilentlyContinue

if (-not $atlasCommand) {
    Write-Error "Atlas CLI no está instalado o no está disponible en PATH."
    exit 1
}

Write-Host "Atlas CLI encontrado:"
Write-Host "  $($atlasCommand.Source)"

# ------------------------------------------------------------
# 2. Detectar automáticamente el Project ID
# ------------------------------------------------------------

Write-Host ""
Write-Host "Buscando proyectos disponibles en MongoDB Atlas..."

$projectsJson = & atlas projects list --output json

if ($LASTEXITCODE -ne 0) {
    Write-Error "No se pudieron obtener los proyectos de MongoDB Atlas."
    exit 1
}

try {
    $projectsResponse = $projectsJson | ConvertFrom-Json
}
catch {
    Write-Error "Atlas CLI devolvió una respuesta JSON no válida."
    exit 1
}

$projects = @($projectsResponse.results)

if ($projects.Count -eq 0) {
    Write-Error "No se encontraron proyectos accesibles en MongoDB Atlas."
    exit 1
}

# ------------------------------------------------------------
# Solo existe un proyecto
# ------------------------------------------------------------

if ($projects.Count -eq 1) {

    $ProjectId = $projects[0].id
    $ProjectName = $projects[0].name

    Write-Host ""
    Write-Host "Proyecto detectado automáticamente:"
    Write-Host "  Nombre : $ProjectName"
    Write-Host "  ID     : $ProjectId"
}

# ------------------------------------------------------------
# Existen varios proyectos
# ------------------------------------------------------------

else {

    Write-Host ""
    Write-Host "Se encontraron varios proyectos:"
    Write-Host ""

    for ($i = 0; $i -lt $projects.Count; $i++) {
        Write-Host "[$($i + 1)] $($projects[$i].name)"
        Write-Host "    $($projects[$i].id)"
    }

    Write-Host ""

    $selection = Read-Host "Selecciona el numero del proyecto"

    $selectionNumber = 0

    if (
        -not [int]::TryParse(
            $selection,
            [ref]$selectionNumber
        ) -or
        $selectionNumber -lt 1 -or
        $selectionNumber -gt $projects.Count
    ) {
        Write-Error "Seleccion de proyecto no válida."
        exit 1
    }

    $selectedProject = $projects[$selectionNumber - 1]

    $ProjectId = $selectedProject.id
    $ProjectName = $selectedProject.name

    Write-Host ""
    Write-Host "Proyecto seleccionado:"
    Write-Host "  Nombre : $ProjectName"
    Write-Host "  ID     : $ProjectId"
}

# ------------------------------------------------------------
# 3. Guardar el proyecto como predeterminado en Atlas CLI
# ------------------------------------------------------------

Write-Host ""
Write-Host "Configurando proyecto predeterminado en Atlas CLI..."

& atlas config set project_id $ProjectId

if ($LASTEXITCODE -ne 0) {
    Write-Error "No se pudo configurar el Project ID en Atlas CLI."
    exit 1
}

Write-Host "Project ID configurado correctamente: $ProjectId"

# ------------------------------------------------------------
# 4. Calcular fecha de expiración
# ------------------------------------------------------------

$deleteAfter = (Get-Date).ToUniversalTime().AddHours($Hours).ToString("yyyy-MM-ddTHH:mm:ssZ")

Write-Host ""
Write-Host "Duracion       : $Hours horas"
Write-Host "Expiracion UTC : $deleteAfter"

# ------------------------------------------------------------
# 5. Añadir la IP pública actual
# ------------------------------------------------------------

Write-Host ""
Write-Host "Detectando y autorizando la IP publica actual..."

& atlas accessLists create `
    --currentIp `
    --projectId $ProjectId `
    --comment "Windows local development - temporary access through CLI" `
    --deleteAfter $deleteAfter

if ($LASTEXITCODE -ne 0) {
    Write-Error "No se pudo actualizar la IP Access List."
    exit $LASTEXITCODE
}

# ------------------------------------------------------------
# 6. Mostrar Access List resultante
# ------------------------------------------------------------

Write-Host ""
Write-Host "Acceso temporal configurado correctamente."
Write-Host "La IP actual estara autorizada durante $Hours horas."
Write-Host ""
Write-Host "Access List actual:"
Write-Host ""

& atlas accessLists list `
    --projectId $ProjectId

if ($LASTEXITCODE -ne 0) {
    Write-Warning "La IP fue añadida, pero no se pudo consultar posteriormente la Access List."
}

Write-Host ""