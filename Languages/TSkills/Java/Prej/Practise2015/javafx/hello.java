package javafx;
import javafx.application.*;
import static javafx.application.Application.launch;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
public abstract class hello extends Application{
    Button button;    
    public static void main(String[] args){
        launch(args);
    }
    public void start(Stage primaryStage) throws Exception{
        primaryStage.setTitle("Title of the Window");
        button=new Button();
        button.setText("Click Me");
        
        StackPane layout=new StackPane();
        layout.getChildren().add(button);
        
        Scene scene=new Scene(layout,300,250);
        primaryStage.show();
    }
}
