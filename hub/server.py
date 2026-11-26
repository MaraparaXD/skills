from mcp.server.fastmcp import FastMCP
from hub.catalog import list_entries, search_entries, read_entry

mcp = FastMCP("Engineering Skills Hub")

@mcp.tool()
def list_skills(category: str = "", include_legacy: bool = False) -> list[dict]:
    """List curated skill metadata; opt in to see unreviewed legacy entries."""
    return list_entries(category, include_legacy)

@mcp.tool()
def search_skills(query: str, include_legacy: bool = False) -> list[dict]:
    """Find relevant playbooks by keywords; return at most ten metadata records."""
    return search_entries(query, include_legacy)

@mcp.tool()
def read_skill(skill_id: str, offset: int = 0, include_legacy: bool = False) -> dict:
    """Read one explicitly selected playbook in bounded chunks. No commands are executed."""
    return read_entry(skill_id, offset, include_legacy)

if __name__ == "__main__":
    mcp.run(transport="stdio")
