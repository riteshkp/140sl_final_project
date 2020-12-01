get_intersections_prices <- function(df, ma_type = "SMA", n = 20){
  
  ## Check for valid input format.
  if(ncol(df) != 8){
    stop("Invalid Data Frame object format given.")
  } else if(!(ma_type %in% c("SMA", "EMA", "WMA"))){
    stop("Invalid MA type given.")
  } else if(!(is.integer(n) | n > 0)){
    stop("Invalid window given.")
  }
  
  threshold <- 1.0
  actions <- c()
  dates <- c()
  
  ## Compute MA
  if(ma_type == "SMA"){
    ma <- SMA(df[,8], n)
  } else if(ma_type == "EMA"){
    ma <- EMA(df[,8], n)
  } else {
    ma <- WMA(df[,8], n)
  }
  
  starting_index <- sum(is.na(ma)) + 1
  
  for (i in starting_index:(nrow(df)-1)){
    cur_price <- df[i, 8]
    cur_ma = ma[i]
    next_price <- df[i+1, 8]
    next_ma = ma[i+1]
    if(cur_price*threshold < cur_ma & next_price > threshold*next_ma){
      actions <- c(actions, 'buy')
      date <- as.character(df[i+1, 1])
      dates <- c(dates, date)
    } else if(cur_price > threshold*cur_ma & next_price*threshold < next_ma){
      actions <- c(actions, 'sell')
      date <- as.character(df[i+1, 1])
      dates <- c(dates, date)
    }
  }
  
  if(length(dates) == 0){
    stop("No dates found.")
  }
  
  return(data.frame(
    dates = as.Date(dates),
    action = actions
  ))
}


get_intersections_sentiment <- function(df, ma_type = "SMA", n = 20){
  
  ## Check for valid input format.
  if(ncol(df) != 8){
    stop("Invalid Data Frame object format given.")
  } else if(!(ma_type %in% c("SMA", "EMA", "WMA"))){
    stop("Invalid MA type given.")
  } else if(!(is.integer(n) | n > 0)){
    stop("Invalid window given.")
  }
  
  ## Compute MA
  if(ma_type == "SMA"){
    ma_sentiment <- SMA((df[,2]-mean(df[,2]))/sd(df[,2]), n)*IQR(df[,6]) + mean(df[,6])
  } else if(ma_type == "EMA"){
    ma_sentiment <- EMA((df[,2]-mean(df[,2]))/sd(df[,2]), n)*IQR(df[,6]) + mean(df[,6])
  } else {
    ma_sentiment <- WMA((df[,2]-mean(df[,2]))/sd(df[,2]), n)*IQR(df[,6]) + mean(df[,6])
  }
  
  actions <- c()
  dates <- c()
  starting_index <- sum(is.na(ma_sentiment)) + 1
  
  for (i in starting_index:(nrow(df)-1)){
    threshold <- 1.2
    cur_price <- df[i, 8]
    cur_sent <- ma_sentiment[i]
    if(cur_price*threshold < cur_sent){
      actions <- c(actions, 'buy')
      date <- as.character(df[i+1, 1])
      dates <- c(dates, date)
    } else if(cur_price > threshold*cur_sent){
      actions <- c(actions, 'sell')
      date <- as.character(df[i+1, 1])
      dates <- c(dates, date)
    }
  }
  if(length(dates) == 0){
    return("Error: No intersections found")
  }
  return(data.frame(
    dates = as.Date(dates),
    action = actions
  ))
}