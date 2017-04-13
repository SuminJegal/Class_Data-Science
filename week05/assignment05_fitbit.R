setwd("/Users/jegalsumin/Documents/Data Science/Class_Data-Science/week05")

library(data.table)
library(ggplot2)
library(plyr)
library(grid)
library(plotly)

#과제 1
personal_total_steps_csv <- read.csv("personal_total_steps.csv")
personal_total_steps_csv[1:10,]

top10_steps <- (arrange(personal_total_steps_csv, desc(step_count)))[1:10,]
top10_steps

bar_top10 <- ggplot(data=top10_steps, aes(x=Person, y=step_count, fill=Person)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  geom_text(aes(label=step_count), vjust=1.6, color="white",position = position_dodge(0.9), size=3.0) +
  scale_y_continuous(labels = scales::comma)
bar_top10

#과제 2
personal_total_hearts_csv <- read.csv("personal_total_hearts.csv")
personal_total_hearts_csv

personal_total = merge(personal_total_hearts_csv,personal_total_steps_csv,key='Person')

total_graph <- plot_ly() %>%
  add_bars(x=personal_total$Person, y=personal_total$step_count, name='steps') %>%
  add_markers(x=personal_total$Person, y=personal_total$heart_total_minutes, name='hearts', yaxis='y2') %>%
  add_lines(x=personal_total$Person, y=personal_total$heart_total_minutes, name='hearts', yaxis='y2') %>%
  layout(yaxis2 = list(tickfont = list(color = 'red'), overlaying='y', side='right', title = 'heart total time'), xaxis=list(title='Person'))
total_graph

personal_total <- cbind(personal_total,(personal_total$step_count*0.01)-personal_total$heart_total_minutes)
colnames(personal_total)[4] <- "sub_heart_step"

lg <- ggplot(data=personal_total, aes(x=Person, y=sub_heart_step)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  scale_y_continuous(labels = scales::comma)
lg