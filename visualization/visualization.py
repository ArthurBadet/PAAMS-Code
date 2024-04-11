from pathlib import Path

from mesa.visualization.ModularVisualization import VisualizationElement

class ContinuousCanvas(VisualizationElement):
    local_includes = [str(Path("visualization", "canvas.js").resolve())]

    def __init__(self, portrayal_method, canvas_width, canvas_height):
        self.portrayal_method = portrayal_method
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        new_element = f"new continuousSpace({self.canvas_width}, {self.canvas_height})"
        self.js_code = f"elements.push({new_element});"

    def render(self, model):
        space_state = []
        for agent in model.schedule.agents:
            portrayal = self.portrayal_method(agent)
            x, y = agent.pos
            #x = ((x - model.space.x_min) / (model.space.x_max - model.space.x_min))
            #y = ((y - model.space.y_min) / (model.space.y_max - model.space.y_min))
            portrayal["x"] = x
            portrayal["y"] = y
            space_state.append(portrayal)
        return space_state
