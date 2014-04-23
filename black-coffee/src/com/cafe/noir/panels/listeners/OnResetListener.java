package com.cafe.noir.panels.listeners;

import javafx.event.EventHandler;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

import com.cafe.noir.arriere.ArriereLeftPanel;
import com.cafe.noir.avant.AvantLeftPanel;
import com.cafe.noir.dialogs.OverwriteDialog;
import com.cafe.noir.dialogs.SaveDialog.Response;
import com.cafe.noir.util.FrameType;
import com.cafe.noir.util.manager.ArriereDataManager;
import com.cafe.noir.util.manager.AvantDataManager;

public class OnResetListener implements EventHandler<MouseEvent>
{
	private FrameType ft;
	
	public OnResetListener( FrameType ft )
	{
		this.ft = ft;
	}
	@Override
	public void handle( MouseEvent arg0 )
	{
		Response resp = OverwriteDialog.showConfirmDialog( new Stage(), 
				"Doing this will reset your work in progress. Are you sure?", "Reset Warning" );
		if( resp == Response.YES )
		{
			switch( ft )
			{
				case Arriere:
					ArriereLeftPanel.listPanel.getListModel().clear();
					ArriereLeftPanel.listPanel.setCurrentListNumber( 0 );
					ArriereDataManager.constructionMap.clear();
					break;
				case Avant:
					AvantLeftPanel.listPanel.getListModel().clear();
					AvantLeftPanel.listPanel.setCurrentListNumber( 0 );
					AvantDataManager.constructionMap.clear();
					break;
				case Manager:
					break;
				case Mobile:
					break;
				default:
					break;
			}
		}
	}

}
