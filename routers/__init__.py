from .classes import router
from .grades import router
from .students import router
from .subjects import router
from .teachers import router
from .teachercls import router

# Makes the folder a proper package
# Allows relative imports
# Lets you re-export things for cleaner imports
# W/o it can’t do from routers import * cleanly