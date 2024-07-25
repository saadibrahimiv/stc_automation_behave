Feature: Subscription Package Validation

  Scenario Outline: Validate subscription packages for <Country>
    Given I navigate to the STC TV subscription page
    When I change the country to "<Country>" and language to "en"
    Then I should see the following subscription packages:
      | Type    | Price | Currency |
      | LITE    | <Price_LITE> | <Currency_LITE> |
      | CLASSIC | <Price_CLASSIC> | <Currency_CLASSIC> |
      | PREMIUM | <Price_PREMIUM> | <Currency_PREMIUM> |

  Examples:
    | Country | Price_LITE | Currency_LITE | Price_CLASSIC | Currency_CLASSIC | Price_PREMIUM | Currency_PREMIUM |
    | sa      | 15         | SAR           | 25            | SAR              | 60            | SAR              |
    | kw      | 1.2        | KWD           | 2.5           | KWD              | 4.8           | KWD              |
    | bh      | 2          | BHD           | 3             | BHD              | 6             | BHD              |
