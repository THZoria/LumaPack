from github import Github
import os
import requests
import zipfile
import shutil

# LumaPack-Vanilla Fetcher
# Script By Zoria/SaoriYuki

#Credit a Shadow256


folder = "gm9"
source_folder = "SD"
destination_zip = 'LumaPack-Vanilla_Latest.zip'
CheckPoint = "BernardoGiordano/Checkpoint"
RELEASE_TAG = "v3.7.3"

# Créer le dossier temp s'il n'existe pas
if not os.path.exists("temp"):
    os.makedirs("temp")

# Créer le dossier SD s'il n'existe pas
if not os.path.exists("SD"):
    os.makedirs("SD")

# Créer le dossier 3ds dans le dossier SD s'il n'existe pas
    if not os.path.exists(os.path.join("SD", "3ds")):
        os.makedirs(os.path.join("SD", "3ds"))

# Créer le dossier cias dans le dossier SD s'il n'existe pas
    if not os.path.exists(os.path.join("SD", "cias")):
        os.makedirs(os.path.join("SD", "cias"))

# Créer le dossier luma dans le dossier SD s'il n'existe pas
if not os.path.exists(os.path.join("SD", "luma")):
    os.mkdir(os.path.join("SD", "luma"))

# Créer le dossier payload dans le dossier luma du dossier SD s'il n'existe pas
if not os.path.exists("SD/luma/payloads"):
    os.makedirs("SD/luma/payloads")

# Créer le dossier payload dans le dossier luma du dossier SD s'il n'existe pas
if not os.path.exists("SD/boot9strap"):
    os.makedirs("SD/boot9strap")
    

# Remplacez "votre_token" par votre propre token d'accès généré depuis votre compte GitHub
token = "votre_token"

# Se connecter à l'API GitHub avec l'authentification par token
g = Github(token)

# Liste des dépôts à interroger
repos = ["LumaTeam/Luma3DS", "d0k3/GodMode9", "ihaveamac/ctr-no-timeoffset", "Steveice10/FBI",
         "PabloMK7/homebrew_launcher_dummy", "astronautlevel2/Anemone3DS", "SciresM/boot9strap", "Universal-Team/Universal-Updater",
         "BernardoGiordano/Checkpoint"]

# Télécharger les fichiers de la dernière version de chaque dépôt dans le dossier "temp"
for repo_name in repos:
    repo = g.get_repo(repo_name)
    if repo_name == "BernardoGiordano/Checkpoint":
        # Récupérer la release v3.7.3
        release = repo.get_release("v3.7.3")
        assets = release.get_assets()
    else:
        latest_release = repo.get_latest_release()
        assets = latest_release.get_assets()

    for asset in assets:
        if asset.name.endswith((".cia", ".3dsx", ".zip")):
            download_url = asset.browser_download_url

            # Télécharger le fichier dans le dossier "temp"
            filename = os.path.join("temp", asset.name)
            with open(filename, "wb") as f:
                response = requests.get(download_url)
                f.write(response.content)
                
            # Décompresser le fichier s'il s'agit d'un fichier zip
            if asset.name.endswith(".zip"):
                with zipfile.ZipFile(filename, 'r') as zip_ref:
                    zip_ref.extractall("temp")
                    
            # Déplacer le fichier dans le dossier "SD/3ds" s'il s'agit d'un fichier ".3dsx"
            if asset.name.endswith(".3dsx"):
                destination_folder = os.path.join("SD", "3ds")
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(filename, os.path.join(
                    destination_folder, os.path.basename(filename)))

            # Déplacer le fichier dans le dossier "SD/cias" s'il s'agit d'un fichier ".cia"
            if asset.name.endswith(".cia"):
                destination_folder = os.path.join("SD", "cias")
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(filename, os.path.join(
                    destination_folder, os.path.basename(filename)))

    # Afficher le nom du dépôt et la version la plus récente
    print(f"{repo_name} - Dernière version: {latest_release.tag_name}")

# Télécharger le fichier 3hs.cia dans le dossier "temp"
url = "https://download2.erista.me/3hs/3hs.cia"
filename = os.path.join("temp", "3hs.cia")
with open(filename, "wb") as f:
    response = requests.get(url)
    f.write(response.content)


# Déplacer le fichier dans le dossier "SD/cias"
destination_folder = os.path.join("SD", "cias")
os.makedirs(destination_folder, exist_ok=True)
shutil.move(filename, os.path.join(destination_folder, os.path.basename(filename)))

    # Afficher le nom du dépôt et la version la plus récente
print(f"{repo_name} - Dernière version: {latest_release.tag_name}")

# Déplacer le fichier dans le dossier "SD/luma/payload" s'il s'agit de GodeMode9 (GodMode9.firm)
filename = "GodMode9.firm"
if (os.path.exists(os.path.join("temp", filename))):
    destination_folder = os.path.join("SD", "luma", "payloads")
    os.makedirs(destination_folder, exist_ok=True)
    shutil.move(os.path.join("temp", filename), os.path.join(
        destination_folder, os.path.basename(filename)))

# Déplacer le fichier dans le dossier "SD" s'il s'agit de Luma3DS (boot.firm)
filename = "boot.firm"
if (os.path.exists(os.path.join("temp", filename))):
    destination_folder = os.path.join("SD")
    os.makedirs(destination_folder, exist_ok=True)
    shutil.move(os.path.join("temp", filename), os.path.join(
        destination_folder, os.path.basename(filename)))

# Déplacer le fichier dans le dossier "SD" s'il s'agit de Luma3DS (boot.3dsx)
filename = "boot.3dsx"
if (os.path.exists(os.path.join("temp", filename))):
    destination_folder = os.path.join("SD")
    os.makedirs(destination_folder, exist_ok=True)
    shutil.move(os.path.join("temp", filename), os.path.join(
        destination_folder, os.path.basename(filename)))

# Déplacer le fichier dans le dossier "SD" s'il s'agit de Boot9Strap (boot9strap.firm)
filename = "boot9strap.firm"
if (os.path.exists(os.path.join("temp", filename))):
    destination_folder = os.path.join("SD", "boot9strap")
    os.makedirs(destination_folder, exist_ok=True)
    shutil.move(os.path.join("temp", filename), os.path.join(
        destination_folder, os.path.basename(filename)))

# Déplacer le fichier dans le dossier "SD" s'il s'agit de Boot9Strap (boot9strap.sha)
filename = "boot9strap.firm.sha"
if (os.path.exists(os.path.join("temp", filename))):
    destination_folder = os.path.join("SD", "boot9strap")
    os.makedirs(destination_folder, exist_ok=True)
    shutil.move(os.path.join("temp", filename), os.path.join(
        destination_folder, os.path.basename(filename)))
    
# Déplacer le dossier gm9 dans le dossier "SD"
if os.path.exists(os.path.join("temp", folder)):
    destination_folder = "SD"
    os.makedirs(destination_folder, exist_ok=True)
    shutil.move(os.path.join("temp", folder),
                os.path.join(destination_folder, folder))
    
    # Compression du dossier source dans le fichier ZIP de destination
with zipfile.ZipFile(destination_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            zip_file.write(os.path.join(root, file), os.path.relpath(
                os.path.join(root, file), source_folder))
            # Suppression des dossiers temp et SD
shutil.rmtree("temp")
shutil.rmtree("SD")
print("Le LumaPack-Vanilla a été généré")
