# simulator.py
from visual_grid_game import VisualGridHuntGame
from agent import GreedyGridAgent

def run_grid_hunt():
    env = VisualGridHuntGame()
    agent = GreedyGridAgent()

    print("=== UC Berkeley Style Small Grid Hunt Started ===")
    while not env.is_done():
        percept = env.get_percept()
        action = agent.sense_and_act(percept)
        env.execute_action(action)
        print(f"Pos: {percept['agent_pos']} | Food Left: {percept['remaining_food']} | Score: {percept['score']} | Smells Food: {percept['smells_food']} | Smells Toxin: {percept['smells_toxin']}")

    print(f"\nGame Over! Final Score: {env.score} after {env.steps} steps.")
    print(f"Food Remaining: {len(env.food_positions)}")
    print(f"Traps Remaining: {len(env.toxic_traps)}")

if __name__ == "__main__":
    run_grid_hunt()