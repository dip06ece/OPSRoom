import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;

import java.util.concurrent.TimeUnit;
public class TestFile {
    @Test
    public void TestWithFF() throws InterruptedException {
        // Configure Firefox options for headless mode
        FirefoxOptions options = new FirefoxOptions();   // Create Firefox Options
        options.addArguments("--headless");              // Set headless mode
        //Set System Properties and create Driver
        System.setProperty("webdriver.gecko.driver","/Users/macbookpro/Downloads/SeleniumWebDrivers/geckodriver");
        WebDriver driver = new FirefoxDriver(options);   // Create driver with options
        driver.get("https://www.google.com/");           // Load page
        TimeUnit.SECONDS.sleep(5);                // Wait
        WebElement searchBar = driver.findElement(
                By.xpath("//*[@id=\"APjFqb\"]")
        );
        searchBar.sendKeys("This is awesome!");
        searchBar.sendKeys(Keys.ENTER);
        TimeUnit.SECONDS.sleep(5);
        driver.close();
    }
    @Test
    public void TestWithCR() throws InterruptedException {
        // Configure Chrome options for headless mode
        ChromeOptions options = new ChromeOptions();    // Create Chrome Options
        options.addArguments("--headless");             // Set headless mode
        options.addArguments("--disable-gpu");          // Disable GPU acceleration

        //Set system properties and set driver options
        System.setProperty("webdriver.chrome.driver","/Users/macbookpro/Downloads/SeleniumWebDrivers/chromedriver");
        WebDriver driver = new ChromeDriver(options);   //New crome driver with options
        driver.get("https://www.google.com/");          // Load page
        TimeUnit.SECONDS.sleep(5);
        WebElement searchBar = driver.findElement(
                By.xpath("//*[@id=\"APjFqb\"]")
        );
        searchBar.sendKeys("This is awesome!");
        searchBar.sendKeys(Keys.ENTER);
        TimeUnit.SECONDS.sleep(5);
        driver.close();
    }
}
