from Pages.base_page import BasePage
from Locators.locators import AdminPageLocators
from selenium.webdriver.common.by import By
from datetime import datetime
from typing import List

class AdminPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        # url of this page
        self.driver.get(self.url)

        # optionaPanel
        self.optional_panels: List(OptionalPanel) = []

    ## Personal info part
    def enter_name(self, name):
        self.enter_text(AdminPageLocators.name_field, name)

    def enter_mail(self, email):
        self.enter_text(AdminPageLocators.email_field, email)

    def name(self):
        """ get typed name"""
        return self.get_text(AdminPageLocators.name_field)

    def email(self):
        """ get typed email"""
        return self.get_text(AdminPageLocators.email_field)


    def set_flux_agenda(self):
        """toggle"""
        # if is not selected yet:
        locator = AdminPageLocators.agenda_flux_switch
        if(not self.is_selected(locator)):
            self.click(locator)

    def has_flux_agenda(self):
        return self.is_selected(AdminPageLocators.agenda_flux_switch)

    def enter_ics_url(self, url):
        self.enter_text(AdminPageLocators.isc_field, url)

    def ics_url(self):
        return self.get_text(AdminPageLocators.isc_field)


    def has_pref_alim(self):
        return self.is_selected(AdminPageLocators.pref_alimentaire_switch)

    def set_pref_alimentaire(self):
        """toggle"""
        # if is not selected yet:
        locator = AdminPageLocators.pref_alimentaire_switch
        if(not self.is_selected(locator)):
            self.click(locator)


    ## Agenda part ##

    def set_optional_panels(self):

        # prepare custom path

        ths = self.get_elements((By.XPATH, "//table//tr[2]//th"))
        size = len(ths)
        infos = []
        # get data from IHM
        # get date
        # date is the first tr
        for i in range(3):
            inner_infos = []
            for j in range(size):
                value = self.get_value((By.XPATH, f"//table//tr[{i+1}]//th[{j+2 if (i ==0 or i == 2) else j+1}]"))
                inner_infos.append(value)
            
            infos.append(inner_infos)

        
        # add optional panel
        # same size of all
        for i in range(len(infos[0])):
            date = infos[0][i]
            start, end = infos[1][i].split('\n-\n')
            participant = int(infos[2][i])

            # add optional component
            self.optional_panels.append(OptionalPanel(date, start, end, participant))



    def chose_vue_calendar(self):
        """chose the calendar vue for time"""
        self.click(AdminPageLocators.vue_calendar_btn)

    def chose_vue_table(self):
        """chose the table vue of time"""
        self.click(AdminPageLocators.vue_table_btn)


    ## Comments part ##

    def enter_comment_author(self, value):
        self.enter_text(AdminPageLocators.author_cmt_field, value)

    def enter_comment_content(self, value):
        self.enter_text(AdminPageLocators.cmt_content_field, value)

    def add_comment(self):
        self.click(AdminPageLocators.add_cmt_btn)




 # component class
class OptionalPanel():
    def __init__(self, date: str, start_time: str, end_time: str, participant: int) -> None:
        self._date = date
        self._start_time = datetime.strptime(start_time, '%H:%M').time()
        self._end_time = datetime.strptime(end_time, '%H:%M').time()
        self._participant = participant

    @property
    def date(self):
        return self._date

    @property
    def start_date(self):
        return self._start_time


    @property
    def end_date(self):
        return self._end_time

    @property
    def participants(self):
        return self._participant




