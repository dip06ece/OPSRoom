import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

import static java.lang.Thread.sleep;

public class SeleniumTest {
    public static void main(String[] args){
        //fucntionClickElementByID();
    }
    @Test
    public void fucntionClickElementByID() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "/Users/macbookpro/Downloads/chromedriver-mac-x64/chromedriver");
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.selenium.dev/selenium/web/web-form.html");
        WebElement text_input = driver.findElement(By.id("my-text-id"));
        text_input.click();
        text_input.sendKeys("Dip Ranjon Das");

        WebElement password = driver.findElement(By.name("my-password"));
        password.click();
        password.sendKeys("APass123");

        WebElement textArea = driver.findElement(By.name("my-textarea"));
        textArea.click();
        textArea.sendKeys("This is a very large text area of more than 1000 words....");

        // Check a Autocomplete Field
        WebElement autoCompleteDataList = driver.findElement(By.name("my-datalist"));
        autoCompleteDataList.click();
        autoCompleteDataList.sendKeys("San Francisco");
        Actions action = new Actions(driver);
        action.sendKeys(Keys.ARROW_DOWN).build().perform();
        // I need to improve here. Can not get the right element





//        WebElement submitButton = driver.findElement(By.className("btn"));
//        submitButton.click();

        //driver.quit();
    }

}
