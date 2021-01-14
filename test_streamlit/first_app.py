import streamlit as st
import numpy as np
import pandas as pd

## Add a title
st.title('My first app')

## Add text
st.write("Here's our first attempt at using data to create a table:")

## Add a df
st.write(pd.DataFrame({
    'first_col': [1,2,3,4],
    'second_col': [10,20,30,40]
}))


## Produce same as above with the code below
"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

## When st sees variable or literal val on its own line,
  ## auto writes it with st.write()
df

## Draw a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data)

## Plot a map
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

## Use widgets for interactivity
## Example: checkboxes
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

## Can move widgets to sidebar
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

## Can use st.beta_columns to layout widgets side by side
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

## Use st.beta_expander to hide large content
expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


## Show progress for long running computations
import time
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

