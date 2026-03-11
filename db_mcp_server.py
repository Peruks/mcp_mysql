from mcp.server.fastmcp import FastMCP
from db_tools import list_databases, list_tables, describe_table, run_query, get_schema
from db_tools import generate_chart

mcp = FastMCP("mysql-tools")


@mcp.tool()
def show_databases():
    """List all databases"""
    return list_databases()


@mcp.tool()
def show_tables():
    """List tables in the database"""
    return list_tables()


@mcp.tool()
def describe_table_tool(table_name: str):
    """Describe table structure"""
    return describe_table(table_name)


@mcp.tool()
def database_schema():
    """Get full database schema"""
    return get_schema()


@mcp.tool()
def run_sql(query: str):
    """Run SQL query"""
    return run_query(query)





if __name__ == "__main__":
    print("Starting MySQL MCP Server...")
    mcp.run()