# AI SQL Analytics using MCP

This project demonstrates how AI can interact with databases using the Model Context Protocol (MCP).

Users can ask questions in natural language, which are translated into SQL queries and executed on a MySQL database.

## Architecture

User Query → Claude AI → MCP Server → MySQL → Data Processing → Visualization → Insights

## Tech Stack

Python  
MySQL  
Model Context Protocol (MCP)  
Claude AI  
Matplotlib  

## Features

• Natural language database queries  
• Automatic SQL generation  
• MySQL database integration  
• Data visualization  
• AI generated insights  

## Example Queries

Show revenue by film category

Which customers spend the most money?

Find monthly rental trends

## Run MCP Server

```bash
python db_mcp_server.py