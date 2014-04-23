package com.cafe.noir.panels.listeners;

import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.input.MouseEvent;

import com.cafe.noir.panels.ListPanel;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.manager.ArriereDataManager;
import com.cafe.noir.util.manager.AvantDataManager;

public class OnFireListener implements EventHandler<MouseEvent>
{
	private ListView<String> list;
	private ObservableList<String> listModel;
	private Button runAllButton;
	private ListPanel listPanel;
	private FrameType frameType;
	
	public OnFireListener( ListView<String> list, ObservableList<String> listModel, Button runAllButton, ListPanel listPanel, FrameType ft )
	{
		this.list = list;
		this.listModel = listModel;
		this.runAllButton = runAllButton;
		this.listPanel = listPanel;
		this.frameType = ft;
	}

	@Override
	public void handle( MouseEvent event ) 
	{
		int index = list.getSelectionModel().getSelectedIndex();
		if( listModel.size() > 0 )
		{
			listModel.remove( index );
			list.getSelectionModel().select( index - 1 );
			listPanel.setCurrentListNumber( listPanel.getCurrentListNumber() - 1 );
			
			if ( listPanel.getCurrentListNumber() == 0 )
				runAllButton.disarm();
			
			switch( frameType )
			{
				case Arriere:
					ArriereDataManager.constructionMap.remove( index );
					break;
				case Avant:
					AvantDataManager.constructionMap.remove( index );
					break;
				case Mobile:
					break;
				default:
					break;
			}
		}
	}

}
