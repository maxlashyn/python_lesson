from monster_hunter.monster_hunter import PlayerState, Player, Game


def test_player_state_init():
    player_state = PlayerState('Player', 10)
    assert player_state.name == 'Player'
    assert player_state.life == 10


def test_player_init():
    player = Player('Player', 10, 5, 1)
    assert player.name == 'Player'
    assert player.life == 10
    assert player.max_life == 10
    assert player.damage == 5
    assert player.heal == 1


def test_player_is_dead():
    player = Player('Player', 10, 5, 1)
    assert not player.is_dead()
    player.life = 0
    assert player.is_dead()
    player.life = -1
    assert player.is_dead()


def test_player_healing():
    player = Player('Player', 0, 5, 1)
    player.healing()
    assert player.life == player.max_life
    player = Player('Player', 10, 5, 1)
    player.life = 0
    player.healing()
    assert player.life == 1


def test_player_hit():
    player = Player('Player', 10, 5, 1)
    player.hit(5)
    assert player.life == 5
    player.hit(10)
    assert player.life == -5


def test_player_state():
    player = Player('Player_1', 6, 5, 1)
    state = player.state()
    assert isinstance(state, PlayerState)
    assert state.name == 'Player_1'
    assert state.life == 6


def test_player_kick():
    player = Player('Player_1', 6, 5, 1)
    player_2 = Player('Player_2', 10, 5, 1)
    player.kick(player_2)
    assert player_2.life == 5
    player.kick(player_2)
    assert player_2.is_dead()


def test_game_init():
    player = Player('Player_1', 6, 5, 1)
    player_2 = Player('Player_2', 10, 5, 1)
    game = Game(player, player_2)
    assert game.player_one is player
    assert game.player_two is player_2


def test_game_is_not_end():
    player = Player('Player_1', 6, 5, 1)
    player_2 = Player('Player_2', 10, 5, 1)
    game = Game(player, player_2)
    assert not game.is_end()
    player.life = 0
    assert game.is_end()
    assert game.winner() == 'Player_2'
    player.life = 6
    player_2.life = 0
    assert game.is_end()
    assert game.winner() == 'Player_1'
