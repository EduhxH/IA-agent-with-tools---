from ddgs import DDGS


def web_search(query: str) -> str:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=4))
        if not results:
            return "No results found."
        output = []
        for r in results:
            output.append(f"Title: {r['title']}\nSummary: {r['body']}\nURL: {r['href']}")
        return "\n\n".join(output)
    except Exception as e:
        return f"Search error: {str(e)}"