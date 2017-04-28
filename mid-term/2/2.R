library(ggplot2)
library(ggmap)
library(extrafont)
library(scales)
library(data.table)
library(stringr)
library(plyr)
library(grid)
library(plotly)


fitbit <- read.csv("/Users/jegalsumin/Documents/Data Science/Data set/fitbit/personal_total.csv")

total_graph <- plot_ly() %>%
  add_lines(x=fitbit$Date, y=fitbit$step_count, name='steps') %>%
  add_lines(x=fitbit$Date, y=fitbit$sleep_time, name='sleep', yaxis='y2') %>%
  layout(yaxis2 = list(tickfont = list(color = 'red'), overlaying='y', side='right', title = 'sleep mean time'), xaxis=list(title='Date')) +
  scale_x_discrete(breaks = c("2016-04-01","2016-04-15","2015-05-01","2015-05-15"),
                   labels = c("Apr 01","Apr 15","May 01", "May 15"))
total_graph
