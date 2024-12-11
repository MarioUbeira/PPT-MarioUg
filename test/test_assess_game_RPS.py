import pytest
from src.rules import GameResult
from src.main import GameAction, assess_game
from src.agent import PredictAgent

@pytest.mark.draw
def test_draw():
    '''
    Partidas con empate
    '''

    assert GameResult.Tie == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Rock)

    assert GameResult.Tie == assess_game(
        user_action=GameAction.Scissors, 
        computer_action=GameAction.Scissors)

    assert GameResult.Tie == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Paper)

@pytest.mark.rock
def test_rock_loses():
    '''
    Rock pierde con Paper 
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Rock)

@pytest.mark.rock
def test_rock_wins():
    '''
    Rock gana a Scissors
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Rock)

@pytest.mark.paper
def test_paper_loses():
    '''
    Paper pierde con Scissors
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Paper)

@pytest.mark.paper
def test_paper_wins():
    '''
    Paper gana a Rock
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Paper)

@pytest.mark.scissors
def test_scissors_loses():
    '''
    Scissors pierde con Rock 
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Scissors)

@pytest.mark.scissors
def test_scissors_wins():
    '''
    Scissors gana a Paper 
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Scissors)

@pytest.mark.agent
def test_last_matches():
    """
    Comproba o funcionamento do historial (last_matches)
    """
    proba = PredictAgent()
    
    assert len(proba.user_moves) == 0
    
    proba.last_matches(GameAction.Rock)
    assert len(proba.user_moves) == 1
    assert proba.user_moves[-1] == GameAction.Rock