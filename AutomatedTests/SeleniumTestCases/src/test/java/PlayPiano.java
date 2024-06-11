import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;

import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

public class PlayPiano {
    private static final Logger LOGGER = Logger.getLogger(TestFile.class.getName());

    @Test
    public void playPiano() throws InterruptedException {
        // Configure Firefox options for headless mode
        FirefoxOptions options = new FirefoxOptions();   // Create Firefox Options
        //options.addArguments("--headless");              // Set headless mode
        //Set System Properties and create Driver
        System.setProperty("webdriver.gecko.driver","/Users/macbookpro/Downloads/SeleniumWebDrivers/geckodriver");
        WebDriver driver = new FirefoxDriver(options);   // Create driver with options
        driver.get("https://www.musicca.com/piano");           // Load page
        TimeUnit.SECONDS.sleep(5);                // Wait
        WebElement pianoButtonLD = driver.findElement(
                By.xpath("/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div/ul/li[9]/span")
        );
        pianoButtonLD.click();
        //searchBar.sendKeys("This is awesome!");
        //searchBar.sendKeys(Keys.ENTER);
        TimeUnit.SECONDS.sleep(5);
        driver.close();
    }
}
