from shiny import ui, render, App
from shinywidgets import output_widget, render_widget
import pandas as pd
from surprise import Dataset, Reader, SVD, KNNBasic
import json
import math
import numpy as np

app_ui = ui.page_fluid(
    ui.tags.style(
        """
        ul.nav.nav-pills.nav-stacked {
            width: 200px; /* Set the desired width value */
        }
        div.col-sm-4.well {
            width: 300px;
        }
        div.d-flex.gap-3 {
            display: flex;
            justify-content: left;
            align-items: left;
        }
        """
    ),
    ui.navset_pill_list(
        ui.nav(
            "Filtragem colaborativa",
            ui.div(
                ui.input_text(
                    "id_user", "ID do usuário", placeholder="ID (e.g., 222)"
                ),
                ui.input_slider("top_n", "Numero de recs", value=5, min=1, max=10),
                class_="d-flex gap-3"
            ),
        ),
        ui.nav(
            "Notebooks",
            "TBD"
        ),
        ui.nav(
            "Autores",
            ui.output_table("autores"),
        ),
        ui.nav_control(
            ui.a(
                "Código fonte do app",
                href="https://github.com/guipsoares/sme0829",
                target="_blank"
            )
        ),
    ),
)


def server(input, output, session):
    @output
    @render.table
    def autores():
        autores = pd.DataFrame({
            "Nome": ["Guilherme Soares", "Amanda", "Fabiana", "Caique"],
            "NUSP": ["11800862", "DEF456", "GHI789", "JKL012"]
        })
        return autores


app = App(app_ui, server)
