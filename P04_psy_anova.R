# Load csv file in R
library(tidyverse)
library(ggpubr)
library(rstatix)
library("report")
library(ggplot2)
library(see)
library(rstanarm)
library(modelbased)

curr_data = read_csv('C:/Users/yawen/Documents/UM/Psychophysics/Scripts/All_subjects_lum_pt37_anova.csv')
curr_data_pt76 = read_csv('C:/Users/yawen/Documents/UM/Psychophysics/Scripts/All_subjects_lum_pt76_anova.csv')



as.character(curr_data['Condition_grp'])
as.character(curr_data_pt76['Condition_grp'])

curr_data %>%
  group_by(Condition_grp,Luminance) %>%
  get_summary_stats(M_Plum_vs_Base, type = "mean_sd")

curr_data_pt76 %>%
  group_by(Condition_grp,Luminance) %>%
  get_summary_stats(M_Plum_vs_Base, type = "mean_sd")
# Create box plots: 

bxp_M_plum_base <- ggboxplot(
  curr_data, x = "Condition_grp", y = "M_Plum_vs_Base",
  color = "Luminance", palette = "jco",
  short.panel.labs = TRUE
)

# Check outliers
curr_data %>%
  group_by(Condition_grp,Luminance) %>%
  identify_outliers(M_Plum_vs_Base)

curr_data_pt76 %>%
  group_by(Condition_grp,Luminance) %>%
  identify_outliers(M_Plum_vs_Base)
# Check normality

curr_data %>%
  group_by(Condition_grp,Luminance) %>%
  shapiro_test(M_Plum_vs_Base)

curr_data_pt76 %>%
  group_by(Condition_grp,Luminance) %>%
  shapiro_test(M_Plum_vs_Base)

# Create qqplot 

ggqqplot(curr_data, "M_Plum_vs_Base", ggtheme = theme_bw()) +
  facet_grid(Condition_grp ~ Luminance, labeller = "label_both")

aov_results_M_plum_base <- 
aov(M_Plum_vs_Base ~ Luminance * Condition_grp,data=curr_data) %>%
  report()
summary(aov_results_M_plum_base)


ctr_m_plum_base <- estimate_contrasts(aov(M_Plum_vs_Base ~ Luminance * Condition_grp,data=curr_data),contrast = "Luminance",adjust = 'fdr')
means_m_plum_base <- estimate_means(aov(M_Plum_vs_Base ~ Luminance * Condition_grp,data=curr_data),"Luminance")

ggplot(means_m_plum_base, aes(x=Luminance, y=Mean)) +
  geom_line() +
  geom_pointrange(aes(ymin=CI_low, ymax=CI_high)) +
  ylab("Change of Perceived Luminance") +
  xlab("Luminance Condition") +
  theme_bw()


ggplot(curr_data) +
  geom_bar(aes(x=Condition_grp, y=M_Plum_vs_Base,fill=Luminance),alpha = 0.7) +
  geom_errorbar(aes(x=Condition_grp, y = Mean, ymin = CI_low, ymax = CI_high), size = 1, color = "white") +
  theme_grey()


aov_results_pt76_M_plum_base <- 
  aov(M_Plum_vs_Base ~ Luminance * Condition_grp,data=curr_data_pt76) %>%
  report()
summary(aov_results_pt76_M_plum_base)


ctr_m_plum_base_pt76 <- estimate_contrasts(aov(M_Plum_vs_Base ~ Luminance * Condition_grp,data=curr_data_pt76),contrast = "Luminance",adjust = 'fdr')
means_m_plum_base_pt76 <- estimate_means(aov(M_Plum_vs_Base ~ Luminance * Condition_grp,data=curr_data_pt76),"Luminance")

