from huggingface_hub import HfApi

api = HfApi()

models = api.list_models(
    search="legal",
    filter="es",          # idioma: etiqueta "es" (español)
    sort="downloads",
    limit=100,
)

for m in models:
    print(m.id, m.downloads)