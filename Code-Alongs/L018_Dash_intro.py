{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from dash import Dash, html, dcc, callback, Input, Output\n",
    "\n",
    "# Three things needed to create a Dash app basically. Components, Layout, and App (logic)\n",
    "app = Dash(__name__)\n",
    "\n",
    "my_H1 = html.H1(\"My dash application\")\n",
    "my_H2 = html.H2(\"More info\")\n",
    "my_dropdown = dcc.Dropdown(options=[\"Äpple\",\"Päron\",\"Banan\",\"Apelsin\",\"Mango\"], value=\"Mango\")\n",
    "my_dropdown_multi = dcc.Dropdown(options=[\"Äpple\",\"Päron\",\"Banan\",\"Apelsin\",\"Mango\"], multi=True, value=\"Mango\")\n",
    "\n",
    "app.layout = html.Div([my_H1, my_H2, my_dropdown, my_dropdown_multi])\n",
    "\n",
    "# Callbacks are used to update the page when something happens, they are decorators\n",
    "# Calls the function update_heading when the value of my_dropdown changes\n",
    "@callback(\n",
    "    Output(my_H2, component_property='children'),\n",
    "    Input(my_dropdown, component_property='value')\n",
    ")\n",
    "def update_heading2(fruit):\n",
    "    return fruit\n",
    "\n",
    "# If debug true it automatically reloads the page when saved\n",
    "app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
