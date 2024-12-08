from src import Panel, Ruuf, PanelFitter


def main(a, b, x, y) -> int:
    panel = Panel(a, b)
    ruuf = Ruuf(x, y)

    panel_fitter = PanelFitter(panel, ruuf)
    return panel_fitter.fit_count()


if __name__ == '__main__':

    print(main(1, 2, 2, 4))
