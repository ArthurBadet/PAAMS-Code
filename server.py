import mesa
#from mesa.visualization.modules import CanvasGrid
#from mesa.visualization.ModularVisualization import ModularServer
from visualization.visualization import ContinuousCanvas

from model import WSNModel


def agent_portrayal(agent):
    portrayal = {
        "Id": agent.unique_id,
        "Color": agent.color,
        "Filled": "true",
        "Radius": 0.5,
        "Layer": 0,
    }
    return portrayal

def start(scenario, port, open_browser):
    grid = ContinuousCanvas(agent_portrayal, scenario["model"]["width"], scenario["model"]["height"])
    server = mesa.visualization.ModularServer(
        ModelVanet, [grid], "VANET Model", scenario, port
    )
    server.launch(port, open_browser)
