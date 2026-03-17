import logging
from typing import Dict, List

from core_engine import settings
from core_engine.core import Core
from core_engine.plugins import PluginManager
from core_engine.utils import Utils

logger = logging.getLogger(__name__)

def main() -> None:
    """
    Main entry point of the core engine.
    """
    logger.info("Core Engine starting up...")

    core = Core(settings.CORE_CONFIG)
    plugin_manager = PluginManager(core)
    utils = Utils()

    plugin_manager.load_plugins()
    core.start()

    try:
        plugin_manager.run_plugins()
    finally:
        core.stop()
        plugin_manager.save_plugins()

if __name__ == "__main__":
    main()