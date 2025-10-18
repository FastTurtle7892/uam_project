% mapDatabaseData.m
function mapDatabaseData()
    % 데이터베이스 파일 경로
    dbName = 'C:\database\gps.db';
    
    % SQLite 데이터베이스 파일 존재 여부 확인
    if ~isfile(dbName)
        error('SQLite file does not exist at specified location: %s', dbName);
    end
    
    % SQLite 데이터베이스 연결 설정
    conn = sqlite(dbName, 'readonly');
    
    % 테이블 존재 여부 확인
    query = 'SELECT name FROM sqlite_master WHERE type="table"';
    tables = fetch(conn, query);
    disp('Available tables in the database:');
    disp(tables.name);
    
    if ~ismember('Signal', tables.name)
        close(conn);
        error('Table "Signal" does not exist in the database.');
    end
    
    % SQL 쿼리 작성
    tableName = 'Signal';
    query = sprintf('SELECT * FROM %s LIMIT 10', tableName); % 상위 10개 행만 가져오기
    
    % 데이터 가져오기
    data = fetch(conn, query);
    
    % 데이터베이스 연결 종료
    close(conn);
    
    % 데이터 확인
    disp('Data fetched from the database:');
    disp(data);
    
    % 지도 표시
    plotDataOnMap(data);
end

% 지도에 데이터를 표시하는 함수
function plotDataOnMap(data)
    % GUI 생성

    ax = geoaxes;

    geobasemap(ax, 'streets');
    
    % 데이터에서 경도, 위도 추출
    latitudes = data.LAT; % 예시 열 이름 사용
    longitudes = data.LON; % 예시 열 이름 사용
    
    % 지도에 데이터 표시
    geoscatter(ax, latitudes, longitudes, 100, 'red', 'filled');
    % title(ax, '운동장 지도');
end
