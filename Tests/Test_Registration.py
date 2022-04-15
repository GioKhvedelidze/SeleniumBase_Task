from seleniumbase import BaseCase


class RegisterTest(BaseCase):

    def test_open_homepage(self):
        self.open(
            'http://testing.challenge.crocoteam.ge:1110/#/'
        )
        self.assert_title(
            'ტესტ ჩელენჯი'
        )
        self.assert_element_visible(
            'body > app-root > app-register-container > div.wrapper > div'
        )

    def test_geo_towns(self):
        self.open(
            'http://testing.challenge.crocoteam.ge:1110/#/'
        )
        self.assert_element_visible(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__form-input.country-city > div.wrapper__form-input__city > app-shared-select > div > ng-select > div'
        )
        self.click(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__form-input.country-city > div.wrapper__form-input__city > app-shared-select > div > ng-select > div'
        )
        city_list = self.find_elements(
            "//*[starts-with(@class, 'ng-option-label')]"
        )

        for i in city_list:
            print(i.text)

    def test_dates(self):
        self.open(
            'http://testing.challenge.crocoteam.ge:1110/#/'
        )
        self.assert_element_visible(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__form-date > div.wrapper__form-date-year > app-shared-select > div > ng-select > div'
        )
        self.click(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__form-date > div.wrapper__form-date-year > app-shared-select > div > ng-select > div'
        )
        expected_dates = ['2005',
                            '2004',
                            '2003',
                            '2002',
                            '2001',
                            '2000',
                            '1999',
                            '1998',
                            '1997',
                            '1996',
                            '1995',
                            '1994',
                            '1993',
                            '1992',
                            '1991',
                            '1990',
                        ]
        available_dates = self.find_elements("//*[starts-with(@class, 'ng-option-label')]")

        for idx,i in enumerate(available_dates):
            self.assertEqual(expected_dates[idx],i.text)

    def test_mail_input(self):
        self.open(
            'http://testing.challenge.crocoteam.ge:1110/#/'
        )
        self.assert_element_visible(
            '/html/body/app-root/app-register-container/div[2]/form/div[7]/app-shared-input/div/label'
        )
        self.send_keys(
            '/html/body/app-root/app-register-container/div[2]/form/div[7]/app-shared-input/div[1]/input',
            'სადადა'
        )
        self.click(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__account-details > div.wrapper__form-input > app-shared-input > div.input-container > input'
        )
        self.assert_text(
            'არასწორი ფორმატი'
        )
        self.send_keys(
            '/html/body/app-root/app-register-container/div[2]/form/div[7]/app-shared-input/div[1]/input',
            '@'
        )
        self.click(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__account-details > div.wrapper__form-input > app-shared-input > div.input-container > input'
        )
        self.assert_text(
            'არასწორი ფორმატი'
        )
        self.send_keys(
            '/html/body/app-root/app-register-container/div[2]/form/div[7]/app-shared-input/div[1]/input',
            'gmail.com'
        )

    def test_password_input(self):
        self.open(
            'http://testing.challenge.crocoteam.ge:1110/#/'
        )
        self.assert_element_visible(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__account-details > div.wrapper__passwords > div:nth-child(1) > app-shared-input > div.input-container > input'
        )
        self.assert_element_visible(
            '/html/body/app-root/app-register-container/div[2]/form/div[8]/div[3]/div[2]/app-shared-input/div/input'
        )
        self.send_keys(
            '/html/body/app-root/app-register-container/div[2]/form/div[8]/div[3]/div[1]/app-shared-input/div/input',
            'Sportman1'
        )
        self.send_keys(
            '/html/body/app-root/app-register-container/div[2]/form/div[8]/div[3]/div[2]/app-shared-input/div/input',
            'Sportman1'
        )
        self.assert_element_visible(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__account-details > div.warpper__validations > p:nth-child(1)'
        )
        self.assert_element_visible(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__account-details > div.warpper__validations > p:nth-child(2)'
        )
        self.assert_element_visible(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__account-details > div.warpper__validations > p:nth-child(3)'
        )
        self.assert_element_visible(
            'body > app-root > app-register-container > div.wrapper > form > div.wrapper__account-details > div.warpper__validations > p:nth-child(4)'
        )
