package com.wizard.magus;

import java.util.Stack;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.Node;
import javafx.scene.layout.StackPane;

public class Wizard extends StackPane 
{
	  private static final int UNDEFINED = -1;
	  private ObservableList<WizardPage> pages = FXCollections.observableArrayList();
	  private Stack<Integer> history = new Stack<>();
	  private int  curPageIdx = UNDEFINED;
	 
	  protected Wizard( WizardPage... nodes ) 
	  {
	    pages.addAll( nodes );
	    navTo(0);
	  }
	 
	  void nextPage() 
	  {
	    if ( hasNextPage() ) 
	    {
	      navTo( curPageIdx + 1 );
	    }
	  }
	 
	  void priorPage() 
	  {
	    if ( hasPriorPage() ) 
	    {
	      navTo( history.pop(), false );
	    }
	  }
	 
	  boolean hasNextPage() 
	  {
	    return ( curPageIdx < pages.size() - 1 );
	  }
	 
	  boolean hasPriorPage()
	  {
	    return !history.isEmpty();
	  }
	 
	  void navTo(int nextPageIdx, boolean pushHistory) 
	  {
	    if ( nextPageIdx < 0 || nextPageIdx >= pages.size() ) return;
	    if ( curPageIdx != UNDEFINED )
	    {
	      if ( pushHistory ) 
	      {
	        history.push( curPageIdx );
	      }
	    }
	 
	    WizardPage nextPage = pages.get( nextPageIdx );
	    if ( nextPageIdx == 3 )
	    {
	    	nextPage.navSpecial();
	    }
	    curPageIdx = nextPageIdx;
	    getChildren().clear();
	    getChildren().add(nextPage);
	    nextPage.manageButtons();
	  }
	 
	  void navTo( int nextPageIdx ) 
	  {
	    navTo(nextPageIdx, true);
	  }
	 
	  void navTo( String id )
	  {
	    Node page = lookup( "#" + id) ;
	    if (page != null) 
	    {
	      int nextPageIdx = pages.indexOf(page);
	      if (nextPageIdx != UNDEFINED) 
	      {
	        navTo(nextPageIdx);
	      }
	    }
	  }
	 
	  public void finish() {}
	  public void cancel() {}
	}