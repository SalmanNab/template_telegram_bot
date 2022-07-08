from types import SimpleNamespace

from src.utils.keyboard import create_keyboard

keys = SimpleNamespace(
    random_connect=':bust_in_silhouette: Random Connect',
    settings=':gear: Settings',
    I_Love_You_Talkhoon=':red_heart: I Love You Talkhoon',
)

keyboards = SimpleNamespace(
    main=create_keyboard(keys.random_connect, keys.settings, keys.I_Love_You_Talkhoon,),
)
