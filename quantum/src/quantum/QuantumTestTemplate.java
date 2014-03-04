package src.quantum;
import java.util.LinkedHashMap;
import java.util.Map.Entry;
import java.util.Set;

import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

	public class QuantumTestTemplate {
		@Test
		public void quantumUnit() {
			int j = 0;
	        WebDriver driver = new FirefoxDriver();
			try{
				LinkedHashMap<Integer, LinkedHashMap<String, String>> cMap = QuantumDataManager.creatorMap;
				Set<Entry<Integer, LinkedHashMap<String, String>>> cMapEntrySet = cMap.entrySet();
				for(Entry<Integer, LinkedHashMap<String, String>> entry : cMapEntrySet){
					LinkedHashMap<String, String> value = entry.getValue();
					Set<Entry<String, String>> innerEntrySet = value.entrySet();
					for(Entry<String, String> innerEntry : innerEntrySet){
						if(innerEntry.getKey().equals("URL")){
							driver.get(innerEntry.getValue());
						}
						else if(innerEntry.getKey().equals("CLICK")){
							String valueFull = innerEntry.getValue();
			        		String[] valueSplit = valueFull.split(",");
			        		if(valueSplit[1].equals("Class Name")){
			        			if(valueSplit[2].contains(" ")){
						        	WebElement query = driver.findElement(By.cssSelector(valueSplit[0] + "[class='"+valueSplit[2]+"']"));
						        	query.click();
			        			}
			        			else{
						        	WebElement query = driver.findElement(By.className(valueSplit[2]));
						        	query.click();
			        			}
					        }
				        	else if (valueSplit[1].equals("ID")){
				        		WebElement query = driver.findElement(By.id(valueSplit[2]));
				        		query.click();
					        }
				        	else if (valueSplit[1].equals("Link Text")){
				        		WebElement query = driver.findElement(By.linkText(valueSplit[2]));
				        		query.click();
					        }
				        	else if (valueSplit[1].equals("CSS Selector")){
				        		WebElement query = driver.findElement(By.cssSelector(valueSplit[2]));
				        		query.click();
					        }
				        	else if (valueSplit[1].equals("Name")){
				        		WebElement query = driver.findElement(By.name(valueSplit[2]));
				        		query.click();
					        }
				        	else if (valueSplit[1].equals("Partial Link Text")){
				        		WebElement query = driver.findElement(By.partialLinkText(valueSplit[2]));
				        		query.click();
				        	}
				        	else if (valueSplit[1].equals("XPath")){
				        		WebElement query = driver.findElement(By.xpath(valueSplit[2]));
				        		query.click();
				        	}
						}
						else if(innerEntry.getKey().equals("TEXT")){
							String valueFull = innerEntry.getValue();
			        		String[] valueSplit = valueFull.split(",");
			        		if(valueSplit[2].equals("Class Name")){
			        			if(valueSplit[2].contains(" ")){
						        	WebElement query = driver.findElement(By.cssSelector(valueSplit[1] + "[class='"+valueSplit[3]+"']"));
						        	query.sendKeys(valueSplit[0]);
			        			}
			        			else{
						        	WebElement query = driver.findElement(By.className(valueSplit[3]));
						        	query.sendKeys(valueSplit[0]);
			        			}
					        }
				        	else if (valueSplit[2].equals("ID")){
				        		WebElement query = driver.findElement(By.id(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        }
				        	else if (valueSplit[2].equals("Link Text")){
				        		WebElement query = driver.findElement(By.linkText(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        }
				        	else if (valueSplit[2].equals("CSS Selector")){
				        		WebElement query = driver.findElement(By.cssSelector(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        }
				        	else if (valueSplit[2].equals("Name")){
				        		WebElement query = driver.findElement(By.name(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        }
				        	else if (valueSplit[2].equals("Partial Link Text")){
				        		WebElement query = driver.findElement(By.partialLinkText(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
				        	}
				        	else if (valueSplit[2].equals("XPath")){
				        		WebElement query = driver.findElement(By.xpath(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
				        	}
						}
						else if(innerEntry.getKey().equals("SUBMIT")){
							String valueFull = innerEntry.getValue();
			        		String[] valueSplit = valueFull.split(",");
			        		if(valueSplit[2].equals("Class Name")){
			        			if(valueSplit[3].contains(" ")){
						        	WebElement query = driver.findElement(By.cssSelector(valueSplit[1] + "[class='"+valueSplit[3]+"']"));
						        	query.sendKeys(valueSplit[0]);
						        	query.submit();
			        			}
			        			else{
						        	WebElement query = driver.findElement(By.className(valueSplit[3]));
						        	query.sendKeys(valueSplit[0]);
						        	query.submit();
			        			}
					        }
				        	else if (valueSplit[2].equals("ID")){
				        		WebElement query = driver.findElement(By.id(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        	query.submit();
					        }
				        	else if (valueSplit[2].equals("Link Text")){
				        		WebElement query = driver.findElement(By.linkText(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        	query.submit();
					        }
				        	else if (valueSplit[2].equals("CSS Selector")){
				        		WebElement query = driver.findElement(By.cssSelector(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        	query.submit();
					        }
				        	else if (valueSplit[2].equals("Name")){
				        		WebElement query = driver.findElement(By.name(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        	query.submit();
					        }
				        	else if (valueSplit[2].equals("Partial Link Text")){
				        		WebElement query = driver.findElement(By.partialLinkText(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        	query.submit();
				        	}
				        	else if (valueSplit[2].equals("XPath")){
				        		WebElement query = driver.findElement(By.xpath(valueSplit[3]));
					        	query.sendKeys(valueSplit[0]);
					        	query.submit();
				        	}
						}
					}
					System.out.println("Step " + (j+1) + " successful!");
					QuantumCreatorMain.terminal.append("Step " + (j+1) + " successful! \n");
					j++;
				} 
		        driver.quit();
			}
			catch(Exception e){
				QuantumCreatorMain.terminal.append("Step " + (j+1) + " FAILURE! \n");
				QuantumCreatorMain.terminal.append(e.toString());
				System.out.println(e);
				driver.quit();
			}
	    }
}
