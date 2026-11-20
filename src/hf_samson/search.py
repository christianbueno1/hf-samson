from huggingface_hub import HfApi

# Inicializar la API de Hugging Face
api = HfApi()

# print("Buscando modelos legales (español e inglés) utilizando los filtros oficiales...")
print("Usando la API oficial de Hugging Face para buscar modelos con filtros específicos...")

# Búsqueda estructurada usando la firma oficial de list_models
models = api.list_models(
    # search="legal",                     # Busca "legal" en los identificadores/repositorios
    # search="instruct multilingual",
    # search="chat",
    # filter=["text-generation", "es", "gguf"],   # Filtra por tarea de generación de texto y etiqueta de idioma en español (puedes ajustar según requieras)
    # filter=["text-generation", "es", "pytorch"],   # Filtra por tarea de generación de texto y etiqueta de idioma en español (puedes ajustar según requieras)
    # filter=["text-generation", "es"],
    # filter=["text-generation", "transformers", "multilingual"],
    filter=["text-generation", "multilingual"],
    # sort="downloads",                   # Ordena los resultados (valores permitidos: “created_at”, “downloads”, “last_modified”, “likes”, “trending_score”)
    sort="trending_score",
    limit=20                            # Limita el número de elementos devueltos
    # limit=100
)

# Iterar sobre el iterable de resultados ModelInfo
for model in models:
    print(f"🔹 Modelo: {model.id}")
    print(f"   Parametros: {getattr(model, 'safetensors', 'N/A')}")
    print(f"   Descargas: {getattr(model, 'downloads', 'N/A')}")
    print(f"   Likes: {getattr(model, 'likes', 'N/A')}")
    print("-" * 50)