from duckduckgo_search import DDGS

def web_search(query: str) -> str:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=4))
        if not results:
            return "Nenhum resultado encontrado."
        output = []
        for r in results:
            output.append(f"Título: {r['title']}\nResumo: {r['body']}\nURL: {r['href']}")
        return "\n\n".join(output)
    except Exception as e:
        return f"Erro na pesquisa: {str(e)}"