package org.example.firefox;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        //My Selenium PlayGround
        System.setProperty("webdriver.gecko.driver","/Users/macbookpro/Downloads/SeleniumWebDrivers/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.get("https://www.google.com/");
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