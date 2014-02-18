package quantum;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

	public class QuantumTestTemplate {
		@Test
		public void quantumUnit() {
	        WebDriver driver = new FirefoxDriver();
			try{
	        // Go to the Google Suggest home page
	        driver.get(QuantumDataManager.baseClassURL);
	        for(String [] thisQuery: QuantumDataManager.creationContainer){
	        	if(thisQuery[1].equals("Class Name")){
		        	WebElement query = driver.findElement(By.className(thisQuery[2]));
		        	if(thisQuery[3].equals("Click")){
		        		query.click();
		        		if(thisQuery[5].equals("Get Size")){
		        			query.getSize();
		        		}
		        		else if(thisQuery[5].equals("Get Text")){
		        			query.getText();
		        		}	
		        		else if(thisQuery[5].equals("Is Visible?")){
		        			query.isDisplayed();
		        		}
			        }
		        	if(thisQuery[3].equals("Send Keys")){
		        		query.sendKeys(thisQuery[4]);
		        		if(thisQuery[5].equals("Submit Form")){
		        			query.submit();
		        		}
			       	}
		        }
	        	else if (thisQuery[1].equals("ID")){
	        		WebElement query = driver.findElement(By.id(thisQuery[2]));
	        		if(thisQuery[3].equals("Click")){
		        		query.click();
		        		if(thisQuery[5].equals("Get Size")){
		        			query.getSize();
		        		}
		        		else if(thisQuery[5].equals("Get Text")){
		        			query.getText();
		        		}	
		        		else if(thisQuery[5].equals("Is Visible?")){
		        			query.isDisplayed();
		        		}
			        }
		        	if(thisQuery[3].equals("Send Keys")){
		        		query.sendKeys(thisQuery[4]);
		        		if(thisQuery[5].equals("Submit Form")){
		        			query.submit();
		        		}
			       	}
		        }
	        	else if (thisQuery[1].equals("Link Text")){
	        		WebElement query = driver.findElement(By.linkText(thisQuery[2]));
	        		if(thisQuery[3].equals("Click")){
		        		query.click();
		        		if(thisQuery[5].equals("Get Size")){
		        			query.getSize();
		        		}
		        		else if(thisQuery[5].equals("Get Text")){
		        			query.getText();
		        		}	
		        		else if(thisQuery[5].equals("Is Visible?")){
		        			query.isDisplayed();
		        		}
			        }
		        	if(thisQuery[3].equals("Send Keys")){
		        		query.sendKeys(thisQuery[4]);
		        		if(thisQuery[5].equals("Submit Form")){
		        			query.submit();
		        		}
			       	}
		        }
	        	else if (thisQuery[1].equals("CSS Selector")){
	        		WebElement query = driver.findElement(By.cssSelector(thisQuery[2]));
	        		if(thisQuery[3].equals("Click")){
		        		query.click();
		        		if(thisQuery[5].equals("Get Size")){
		        			query.getSize();
		        		}
		        		else if(thisQuery[5].equals("Get Text")){
		        			query.getText();
		        		}	
		        		else if(thisQuery[5].equals("Is Visible?")){
		        			query.isDisplayed();
		        		}
			        }
		        	if(thisQuery[3].equals("Send Keys")){
		        		query.sendKeys(thisQuery[4]);
		        		if(thisQuery[5].equals("Submit Form")){
		        			query.submit();
		        		}
			       	}
		        }
	        	else if (thisQuery[1].equals("Name")){
	        		WebElement query = driver.findElement(By.name(thisQuery[2]));
	        		if(thisQuery[3].equals("Click")){
		        		query.click();
		        		if(thisQuery[5].equals("Get Size")){
		        			query.getSize();
		        		}
		        		else if(thisQuery[5].equals("Get Text")){
		        			query.getText();
		        		}	
		        		else if(thisQuery[5].equals("Is Visible?")){
		        			query.isDisplayed();
		        		}
			        }
		        	if(thisQuery[3].equals("Send Keys")){
		        		query.sendKeys(thisQuery[4]);
		        		if(thisQuery[5].equals("Submit Form")){
		        			query.submit();
		        		}
			       	}
		        }
	        	else if (thisQuery[1].equals("Partial Link Text")){
	        		WebElement query = driver.findElement(By.partialLinkText(thisQuery[2]));
	        		if(thisQuery[3].equals("Click")){
		        		query.click();
		        		if(thisQuery[5].equals("Get Size")){
		        			query.getSize();
		        		}
		        		else if(thisQuery[5].equals("Get Text")){
		        			query.getText();
		        		}	
		        		else if(thisQuery[5].equals("Is Visible?")){
		        			query.isDisplayed();
		        		}
			        }
		        	if(thisQuery[3].equals("Send Keys")){
		        		query.sendKeys(thisQuery[4]);
		        		if(thisQuery[5].equals("Submit Form")){
		        			query.submit();
		        		}
			       	}
	        	}
	        	else if (thisQuery[1].equals("XPath")){
	        		WebElement query = driver.findElement(By.xpath(thisQuery[2]));
	        		if(thisQuery[3].equals("Click")){
		        		query.click();
		        		if(thisQuery[5].equals("Get Size")){
		        			query.getSize();
		        		}
		        		else if(thisQuery[5].equals("Get Text")){
		        			query.getText();
		        		}	
		        		else if(thisQuery[5].equals("Is Visible?")){
		        			query.isDisplayed();
		        		}
			        }
		        	if(thisQuery[3].equals("Send Keys")){
		        		query.sendKeys(thisQuery[4]);
		        		if(thisQuery[5].equals("Submit Form")){
		        			query.submit();
		        		}
			       	}
	        	}
	        }
	        driver.quit();
			}
			catch(Exception e){
				System.out.println(e);
				driver.quit();
			}
    }
}
