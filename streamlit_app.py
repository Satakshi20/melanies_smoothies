# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your Smoothie!.
    """
)

import streamlit as st

name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your smoothie will be:", name_on_order)


cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)


ingredients_list = st.multiselect(
    "Choose upto 5 ingredients:"
    , my_dataframe
    )
if ingredients_list:
    ingredients_string = ' '

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

    #st.write(my_insert_stmt)
