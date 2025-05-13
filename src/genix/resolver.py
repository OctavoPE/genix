def resolve_command(query: str) -> str:
    """Resolve a natural language query to a shell command."""
    # Placeholder: Will integrate with LLM
    if query.lower() == "set up new repo":
        return "git init"
    raise ValueError("Query not recognized")
