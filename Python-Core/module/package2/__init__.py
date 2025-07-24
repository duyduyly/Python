from .Config import ENV, API_KEY
from .Tools import do_something

# Optional: run some setup
print(f"[my_package] Loaded in {ENV} mode")

# Now expose variables at package level
__all__ = ["ENV", "API_KEY"]