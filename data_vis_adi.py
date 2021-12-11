# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 14:53:06 2021

@author: Aditya Rao
"""

import pydeck as pdk
import pandas as pd
from pydeck.types import String
import os

def filterData(db, print_head=False):
    """
    Parameters
    ----------
    db : string
        csv file path.
    
    print_head : bool
        whether to print the first 5 values of the result dataframe, by default
        this set to false
    
    Returns
    -------
    df_rel : pandas dataframe
        dataframe of filtered data.

    """
    df = pd.read_csv(db)
    df_rel = df[['latitude','longitude','year','source_headline','best']] 
    
    if print_head:
        print(df_rel.head())
    
    return df_rel
    
def generateDeckHex(df,name):
    """
    Parameters
    ----------
    df : pandas dataframe
        dataframe of values to by mapped by deckgl.
    name : string
        name of output file (do not include .html).

    Returns
    -------
    None.

    """
    layer = pdk.Layer(
        'HexagonLayer',  # `type` positional argument is here
        data = df,
        get_position=['longitude', 'latitude'],
        auto_highlight=True,
        get_elevation = 'best',
        radius=20000,
        elevation_scale=150,
        pickable=True,      
        elevation_range=[0, 3000],
        extruded=True,
        tooltip='source_headline',
        coverage=1)
    
    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=34.52813,
        latitude=69.17233,
        zoom=2,
        min_zoom=1,
        max_zoom=100,
        pitch=40.5,
        bearing=0)
    
    # Combined all of it and render a viewport
    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    r.to_html(f'{name}.html')

def generateDeckHeat(df,name):
    """
    Parameters
    ----------
    df : pandas dataframe
        dataframe of values to by mapped by deckgl.
    name : string
        name of output file (do not include .html).

    Returns
    -------
    None.

    """
    layer = pdk.Layer(
        'HeatmapLayer',  # `type` positional argument is here
        data = df,
        get_weight = 'best',
        get_position=['longitude', 'latitude'],
        auto_highlight=True,
        get_elevation = 'best',
        aggregation = String('TOTAL'),
        tooltip='source_headline',
        coverage=1)
    
    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=34.52813,
        latitude=69.17233,
        zoom=2,
        min_zoom=1,
        max_zoom=100,
        pitch=40.5,
        bearing=0)
    
    # Combined all of it and render a viewport
    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    r.to_html(f'{name}.html')

    
if __name__ == "__main__":
    ARMS_TRADE_DB = ('./ArmsTrade/ged211.csv')

    df = filterData(ARMS_TRADE_DB)
    #generateDeck(df,'arms-filtered-8')
    generateDeckHeat(df, 'arms-heat-1')