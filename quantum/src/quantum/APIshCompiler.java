package src.quantum;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.net.URL;
import java.net.URLClassLoader;
import java.security.CodeSource;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import javax.tools.Diagnostic;
import javax.tools.DiagnosticCollector;
import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import javax.tools.StandardJavaFileManager;
import javax.tools.ToolProvider;

public class APIshCompiler {
	public static void compile() {

        File helloWorldJava = new File("APIshScripts/epoch/"+APIshDataManager.className+".java");
        if (helloWorldJava.getParentFile().exists() || helloWorldJava.getParentFile().mkdirs()) {

            try {
                Writer writer = null;
                try {
                    writer = new FileWriter(helloWorldJava);
                    writer.write(APIshConstructor.construct());
                    writer.flush();
                } finally {
                    try {
                        writer.close();
                    } catch (Exception e) {
                    }
                }

                /** Compilation Requirements *********************************************************************************************/
                DiagnosticCollector<JavaFileObject> diagnostics = new DiagnosticCollector<JavaFileObject>();
                JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
                StandardJavaFileManager fileManager = compiler.getStandardFileManager(diagnostics, null, null);

                // This sets up the class path that the compiler will use.
                // I've added the .jar file that contains the DoStuff interface within in it...
                List<String> optionList = new ArrayList<String>();
                optionList.add("-classpath");
                CodeSource src = APIshCompiler.class.getProtectionDomain().getCodeSource();
                if (src != null) {
                  URL jar = src.getLocation();
                      /* Do something with this entry. */
                        optionList.add(System.getProperty("java.class.path") + ":"+jar.toString()+"APIsh.jar");
                }
                //optionList.add(System.getProperty("java.class.path") + "/Users/Zola/Documents/Quantum.jar");

                Iterable<? extends JavaFileObject> compilationUnit
                        = fileManager.getJavaFileObjectsFromFiles(Arrays.asList(helloWorldJava));
                JavaCompiler.CompilationTask task = compiler.getTask(
                    null, 
                    fileManager, 
                    diagnostics, 
                    optionList, 
                    null, 
                    compilationUnit);
                /********************************************************************************************* Compilation Requirements **/
                if (task.call()) {
                    /** Load and execute *************************************************************************************************/
                    System.out.println("Yipe");
                    // Create a new custom class loader, pointing to the directory that contains the compiled
                    // classes, this should point to the top of the package structure!
                    URLClassLoader classLoader = new URLClassLoader(new URL[]{new File("./APIshScripts").toURI().toURL()});
                    // Load the class from the classloader by name....
                    Class<?> loadedClass = classLoader.loadClass("epoch."+APIshDataManager.className);
                    // Create a new instance...
                    Object obj = loadedClass.newInstance();
                    // Santity check
                    //runTestCase(loadedClass);
                    if (obj instanceof DoStuff) {
                        // Cast to the DoStuff interface
                        DoStuff stuffToDo = (DoStuff)obj;
                        // Run it baby
                        stuffToDo.doStuff();
                    }
                    /************************************************************************************************* Load and execute **/
                } else {
                    for (Diagnostic<? extends JavaFileObject> diagnostic : diagnostics.getDiagnostics()) {
                        System.out.format("Error on line %d in %s%n",
                                diagnostic.getLineNumber(),
                                diagnostic.getSource().toUri());
                    }
                }
                fileManager.close();
            } catch (IOException | ClassNotFoundException | InstantiationException | IllegalAccessException exp) {
                exp.printStackTrace();
            }
        }
    }
    public static interface DoStuff {

        public void doStuff();
    }
}
