from google.adk.agents.llm_agent import Agent

def cloud_kitchen_tool(city: str) -> dict:
    """Returns the WestBengal cloud kitchen menu with prices for a given city."""
    menu = {
        "fish curry": "₹1500",
        "rice": "₹50",
        "roti": "₹20",
        "lentil": "₹30",
        "prawns": "₹30",
        "chicken": "₹40",
        "mutton": "₹40"
    }

    if city.strip().lower() == "kolkata":
        return {"status": "success", "city": city, "menu": menu}
    else:
        return {"status": "error", "message": f"Sorry, we don't have a menu for {city} yet."}

def order_confirmation(menu_item : str) -> dict:
    """Returns the order confirmation for a given menu item."""
    return {"status": "success", "menu_item": menu_item}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Provides the WestBengal cloud kitchen menu for Kolkata.",
    instruction="""You are a helpful cloud kitchen assistant.

IMPORTANT: Whenever a user asks about food, menu, dishes, or prices:
- ALWAYS call the 'cloud_kitchen_tool' with the city name first.
- Display the menu returned by the tool in a clean, readable format.
- Do NOT make up or guess menu items — only use what the tool returns.
- If the user doesn't mention a city, ask them which city they are in.
- We currently only serve Kolkata. If another city is requested, inform the user politely.
""",
    tools=[cloud_kitchen_tool,order_confirmation],
)