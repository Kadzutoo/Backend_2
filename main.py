from decouple import Config, RepositoryEnv
from logic import play_game

# Загрузка настроек из settings.ini
config = Config(RepositoryEnv('settings.ini'))

min_value = config('min_value', cast=int)
max_value = config('max_value', cast=int)
attempts = config('attempts', cast=int)
initial_capital = config('initial_capital', cast=int)

if __name__ == "__main__":
    play_game(min_value, max_value, attempts, initial_capital)
