from selenium import webdriver
***************************************TestCase:Validation********************************
#load chrome driver
driver=webdriver.Chrome(executable_path=r"C:\Users\H.A.R\Desktop\Testing\chromedriver.exe")
#go to www.d3a.io
driver.get('https://www.d3a.io')
#click login button
login_button=driver.find_element_by_xpath('//*[@id="root"]/main/header/div/a').click()
#switch url to https://www.d3a.io/login
driver.get('https://www.d3a.io/login')
#Enter email
email=input('Enter a Email Address:')
#Enter password
password=input('Enter a Password:')
#send email 
email_text=driver.find_element_by_xpath('//*[@id="email"]')
email_text.send_keys(email)
#send password
pass_text=driver.find_element_by_xpath('//*[@id="password"]')
pass_text.send_keys(password)
#submit
submit=driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div/div/form/div[3]/button')
submit.click()
***************************************TestCase:Create a Project********************************
#Create a Project
#Click on NewProject Button
new_project_btn=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/div[3]/button[2]/span')
new_project_btn.click()
#Enter a Name
name=input('Enter Project Name:')
#Enter Description
description=input('Enter Project Description:')
#send project project name
name_text=driver.find_element_by_xpath('//*[@id="input-field-name"]')
name_text.send_keys(name)
#send project project description
description_text=driver.find_element_by_xpath('//*[@id="textarea-field-nameTextArea"]')
description_text.send_keys(description)
#Click on ADD
add_btn=driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button')
add_btn.click()
#check added project listed correctly or not
saved_project=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[1]/div[1]')
saved_project.is_displayed()
***************************************TestCase:Create a Simulation********************************
#Click on Expand to add Simulation
expand=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[1]/div[1]/span/div[1]/div/svg')
expand.click()
#Click on SimulationButton
simulation_btn=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/button')
simulation_btn.click()
#Create a Empty Simulation
new_simulation=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/button')
new_simulation.click()
#Check simulation listed correctly or not
saved_simulation=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/p')
saved_simulation.is_displayed()
