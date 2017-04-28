library(XML)
library(tm)
library(dplyr)
library(xtable)
library(wordcloud)
library(RColorBrewer)
library(KoNLP)

speechtext <-function(ymd){
  sotu <-data.frame(matrix(nrow=1, ncol = 3))
  colnames(sotu) = c("speechtext","year","date")
  for(i in 1:length(ymd)){
    year <- substr(ymd[i],1,4)
    url <- paste0('http://stateoftheunion.onetwothree.net/texts/',ymd[i],'.html')
    doc.html = htmlTreeParse(url,useInternal=TRUE)
    
    doc.text = unlist(xpathApply(doc.html,'//p',xmlValue))
    
    doc.text=gsub('\\n',' ',doc.text)
    doc.text=gsub('\\"','',doc.text)
    
    doc.text=paste(doc.text,collapse = '')
    
    x <- data.frame(doc.text, year, ymd[i], stringsAsFactors = FALSE)
    names(x) <- c("speechtext","year","date")
    sotu <-rbind(sotu,x)
    sotu <- sotu[!is.na(sotu$speechtext),]
  }
  return(sotu)
}

sotu <- speechtext(c("20080128","20160112"))

docs <- Corpus(VectorSource(sotu$speechtext)) %>%
  tm_map(removePunctuation) %>%
  tm_map(removeNumbers) %>%
  tm_map(tolower)  %>%
  tm_map(removeWords, stopwords("english")) %>%
  tm_map(stripWhitespace) %>%
  tm_map(PlainTextDocument)

tdm <- TermDocumentMatrix(docs) %>%
  as.matrix()
colnames(tdm) <- c("Bush","Obama")

head(tdm)

##
bushsotu <- as.matrix(tdm[,1])
bushsotu <- as.matrix(bushsotu[order(bushsotu, decreasing=TRUE),])
head(bushsotu)

##
obamasotu <- as.matrix(tdm[,2])
obamasotu <- as.matrix(obamasotu[order(obamasotu, decreasing=TRUE),])
head(obamasotu)


#Create Bush and Obama word clouds and plot them side-by-side
#Create two panels to add the word clouds to
par(mfrow=c(1,2))
wordcloud(rownames(bushsotu), bushsotu, min.freq =3, scale=c(5, .2), random.order = FALSE, random.color = FALSE, colors= c("indianred1","indianred2","indianred3","indianred"))
wordcloud(rownames(obamasotu), obamasotu, min.freq =3, scale=c(5, .2), random.order = FALSE, random.color = FALSE, colors= c("lightsteelblue1","lightsteelblue2","lightsteelblue3","lightsteelblue"))
par(mfrow=c(1,1))
comparison.cloud(tdm, random.order=FALSE, colors = c("indianred3","lightsteelblue3"),
                 title.size=2.5, max.words=400)
commonality.cloud(tdm, random.order=FALSE, scale=c(5, .5),colors = brewer.pal(4, "Dark2"), max.words=400)



#KoNLP
useSejongDic()
conn=file("/Users/jegalsumin/Documents/Data Science/Data set/wordCloud/blog",open="r")
blog_data=readLines(conn)
close(conn)
conn=file("/Users/jegalsumin/Documents/Data Science/Data set/wordCloud/news",open="r")
news_data=readLines(conn)
close(conn)

print(blog_data)

blog_data <- gsub("(\n|<b>|</b>|\\d+|\\(|\\))", "", blog_data)
blog_nouns <- sapply(blog_data, extractNoun, USE.NAMES=F)
blog_c <- unlist(blog_nouns)
blog_nouns <- Filter(function(x) {nchar(x) >= 2}, blog_c)
blog_wordcount <- table(unlist(blog_nouns))
blog_df <- data.frame(blog_wordcount)
blog_pal <- brewer.pal(12,"Set3")
blog_pal <- blog_pal[-c(1:2)]
wordcloud(names(blog_wordcount), freq=wordcount, scale=c(6,0.3), min.freq=25, random.order=T, rot.per=.1, colors=pal, family="NanumGothicOTF")

news_data <- gsub("(\n|<b>|</b>|\\d+|\\(|\\))", "", news_data)
news_nouns <- sapply(news_data, extractNoun, USE.NAMES=F)
news_c <- unlist(news_nouns)
news_nouns <- Filter(function(x) {nchar(x) >= 2}, news_c)
news_wordcount <- table(unlist(news_nouns))
news_df <- data.frame(news_wordcount)
news_pal <- brewer.pal(12,"Set3")
news_pal <- news_pal[-c(1:2)]
wordcloud(names(news_wordcount), freq=wordcount, scale=c(6,0.3), min.freq=25, random.order=T, rot.per=.1, colors=pal, family="NanumGothicOTF")

colnames(blog_df) <- c("word","blog")
colnames(news_df) <- c("word","news")
total_df <- merge(blog_df,news_df,by='word',all=TRUE)
total_df[is.na(total_df)] <- 0
rownames(total_df) <- total_df$word
total_df <- total_df[,-1]
comparison.cloud(total_df, random.order=FALSE, colors = c("indianred3","lightsteelblue3"),
                 title.size=2.5, max.words=400, family="NanumGothicOTF")

commonality.cloud(total_df, random.order=FALSE, scale=c(5, .5),colors = brewer.pal(4, "Dark2"), max.words=400,  family="NanumGothicOTF")
