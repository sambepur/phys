async def display_mouse_coordinates(event) -> tuple[str, str]:
        return f"X: {event.x}", f"Y: {event.y}"