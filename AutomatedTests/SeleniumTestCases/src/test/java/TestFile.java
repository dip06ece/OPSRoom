import io.qameta.allure.testng.AllureTestNg;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Listeners;

import java.util.concurrent.TimeUnit;
import java.util.logging.ConsoleHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
@Listeners(AllureTestNg.class)
public class TestFile {
    private static final Logger LOGGER = Logger.getLogger(TestFile.class.getName());

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
    @AfterTest
    public void testTearDown(){
//        LOGGER.setLevel(Level.INFO);
//        ConsoleHandler consoleHandler = new ConsoleHandler();
//        consoleHandler.setLevel(Level.INFO);
//        LOGGER.addHandler(consoleHandler);
//        System.out.println("One Test Case is executed!...............");

    }
    @BeforeTest
    public void testSetup(){
        LOGGER.setLevel(Level.INFO);
        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(Level.INFO);
        LOGGER.addHandler(consoleHandler);
        System.out.println("One Test Case execution started!...............");
    }
}
