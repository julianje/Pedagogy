
set.seed(29837)

Range = seq(1,10,by=0.05)
ParamA = rep(Range,length(Range))
ParamB = rep(Range,each=length(Range))

Results <- sapply(seq(length(ParamA)),function(x){
  return(prop.table(table(rbeta(10000,ParamA[x],ParamB[x])>rbeta(10000,ParamB[x],ParamA[x])))[2])
  })

Results <- data.frame(Results) %>% tbl_df %>% add_rownames("Id")

Results$ParamA = ParamA
Results$ParamB = ParamB

Results <- Results %>% mutate(Fit=(round(Results,1)==0.8))

Results %>% ggplot(aes(x=ParamA,y=ParamB,color=Fit))+geom_point()+theme_bw()+ 
  scale_color_grey()+scale_x_continuous("Alpha")+scale_y_continuous("Beta")

UsableParameters <- Results %>% filter(Fit)

LeftLimit <- UsableParameters %>% filter(ParamB==min(UsableParameters$ParamB))
mean(LeftLimit$ParamA) # 1.875
mean(LeftLimit$ParamB) # 1

RightLimit <- UsableParameters %>% filter(ParamA==max(UsableParameters$ParamA))
mean(RightLimit$ParamA) # 10
mean(RightLimit$ParamB) # 7.5274

# Plot the distributions:

range = seq(0,1,by=0.01)
data = data.frame(
  Reward = rep(range,6),
  Probabilities=c(dbeta(range,1.875,1),
                  dbeta(range,1,1.875),
                  dbeta(range,10,7.5274),
                  dbeta(range,7.5274,10),
                  dbeta(range,6,4.15),
                  dbeta(range,4.15,6)),
  Distribution=c(rep(rep(c("Light","Music"),each=length(range)),3)),
  Type=c(rep("A",2*length(range)),rep("C",2*length(range)),rep("B",2*length(range)))
)

data %>% ggplot(aes(x=Reward,y=Probabilities,group=Distribution,color=Distribution))+
  geom_line()+theme_bw()+facet_wrap(~Type)

UsableParameters %>% filter(ParamA==6)

# Draw Betas:

ParamA = 1.875
ParamB = 1

ParamA = 10
ParamB = 7.5274

ParamA = 6
ParamB = 4.15

xrange=seq(0,1,by=0.01)
data = data.frame(
  range=rep(xrange,2),
  density=c(dbeta(xrange,ParamA,ParamB),dbeta(xrange,ParamB,ParamA)),
  source=rep(c("Lights","Music"),each=length(xrange))
)
data %>% ggplot(aes(x=range,y=density,group=source,color=source))+geom_line()+theme_bw()
