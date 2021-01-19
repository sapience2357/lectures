#install.packages('ggplot2')
library(ggplot2)

studenth <- c(169, 166.5, 171.6, 177.5, 169.8, 175.4, 176,
              172.1, 172.7, 173, 183.1, 180.5, 173.6, 174.5,
              174.5, 165.8, 170, 176.4, 171.7, 174)

L1_loss <- function(m) {
  sum(abs(studenth - m))
}

temp <- seq(165, 180, length = 1000)

value <- Vectorize(L1_loss)(temp)

ggplot(data = data.frame(x=temp, y=value)) +
  geom_line(aes(x=x, y=y))

set.seed(123)
x <- 10000 #초기자본
p <- 0.47
z <- x
m <- 1000
ruin = numeric(m)

#simulate
for(i in 1:m) {
  j = 0
  repeat {
    y = sample(c(100, -100), 1, prob = c(p, 1-p))
    x = x + y
    # z[i] = x
    if(x <= 0) break
    else {
      j = j + 1
    }
  }
  ruin[i] <- j
  x <- 10000
}

# ggplot(data.frame(trial=1:length(z), money=z)) +
#  geom_line(aes(x=trial, y=money))

ggplot(data.frame(N = ruin)) + 
  geom_histogram(aes(x=N))






