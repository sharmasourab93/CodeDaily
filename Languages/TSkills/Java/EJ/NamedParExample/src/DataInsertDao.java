import java.util.HashMap;
import java.util.Map;

import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;

public class DataInsertDao {

	NamedParameterJdbcTemplate jdbcTemplate;

	public NamedParameterJdbcTemplate getJdbcTemplate() {
		return jdbcTemplate;
	}

	public void setJdbcTemplate(NamedParameterJdbcTemplate jdbcTemplate) {
		this.jdbcTemplate = jdbcTemplate;
	}
	
	public void insertRecord() {
		String sql="insert into employ values(:empno,:name,:dept,:desig,:basic)";
		
		Map namedParameters=new HashMap();
		
		namedParameters.put("empno",new Integer(875));
		namedParameters.put("dept", "Java");
		namedParameters.put("basic",new Integer(88733));
		namedParameters.put("name","Nabin");
		namedParameters.put("desig","Programmer");
		
		jdbcTemplate.update(sql,namedParameters);
		System.out.println("Record Inserted (NamedParametersDemo)");
	}
	
}
